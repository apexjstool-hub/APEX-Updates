#!/usr/bin/env python3
"""Build report v3.1.2 from the existing v3.1.1 update without replacing PDF logic."""
import hashlib, json, pathlib, sys, zipfile
SOURCE = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path("updates/report/APEX-report-3.1.1.apexupdate")
OUT = pathlib.Path("updates/report/APEX-report-3.1.2.apexupdate")
assert SOURCE.is_file(), f"Missing {SOURCE}"
with zipfile.ZipFile(SOURCE) as z:
    data = {n:z.read(n) for n in z.namelist() if not n.endswith("/")}
assert {"manifest.json","module.js","module.css"} <= data.keys()
manifest=json.loads(data["manifest.json"])
assert manifest["module"]=="report" and manifest["version"]=="3.1.1"
js=data["module.js"].decode("utf-8")
needle="const rows = modules.map(([id, name]) => {"
assert js.count(needle)==1
start=js.index(needle); end=js.index("\n    const counts =",start)
chunk=js[start:end]
assert chunk.rstrip().endswith("});")
chunk=chunk.rstrip()[:-3]+"}).filter(row => row.status.key !== 'not-tested');"
js=js[:start]+chunk+js[end:]
anchor="if (counts.fail || advancedBlock === 'fail') {"
assert js.count(anchor)==1
js=js.replace(anchor,"if (!rows.length && advancedBlock === null) {\n      verdict = 'REVIEW REQUIRED'; tone = 'review'; detail = 'No completed diagnostic checks recorded.';\n    } else "+anchor,1)
data["module.js"]=js.encode("utf-8")
manifest["version"]="3.1.2"
manifest["description"]="Report/PDF list only performed diagnostics; preserve FAIL, REVIEW and unverified evidence."
for key in ("installedAt","sourceName","sha256"): manifest.pop(key,None)
data["manifest.json"]=(json.dumps(manifest,indent=2)+"\n").encode()
OUT.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(OUT,"w",zipfile.ZIP_DEFLATED) as z:
    for n,content in data.items(): z.writestr(n,content)
raw=OUT.read_bytes()
print(json.dumps({"version":"3.1.2","file":OUT.as_posix(),"sha256":hashlib.sha256(raw).hexdigest(),"sizeBytes":len(raw)},indent=2))
print("PREVIEW BUILD ONLY: test updater and PDF on Windows before changing latest.json")
