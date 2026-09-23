import json,hashlib,pathlib,platform
import math
alt=300e3;pixel=10e-6;f=1.;gsd=alt*pixel/f;swath=gsd*4096;out={"altitude_m":alt,"pixel_pitch_m":pixel,"focal_length_m":f,"gsd_m_per_pixel":gsd,"swath_m":swath};ok=gsd>0 and swath>gsd
out.update({"farm":138,"engine":"python-engineering-batch-canary","engine_version":platform.python_version(),"test":"GROUND_SAMPLE_DISTANCE","status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"ENGINEERING_CANARY_NOT_PHYSICAL_VALIDATION"});raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f138_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
