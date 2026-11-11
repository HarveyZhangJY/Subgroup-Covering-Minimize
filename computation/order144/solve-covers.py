import json, sys, time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

path = sys.argv[1]
n = int(sys.argv[2])
time_limit = float(sys.argv[3]) if len(sys.argv) > 3 else 60
for line in open(path):
    d = json.loads(line)
    subs = d['subs']
    covered = set().union(*(set(s) for s in subs)) if subs else set()
    if covered != set(range(n*n)):
        print(json.dumps({'id': d['id'], 'exp': d['exp'], 'variables': len(subs), 'cover': None, 'reason': 'uncovered elements'}), flush=True)
        continue
    A = lil_matrix((n*n, len(subs)), dtype=float)
    for j, s in enumerate(subs):
        for e in s:
            A[e, j] = 1
    A = A.tocsr()
    t = time.time()
    res = milp(np.ones(len(subs)), integrality=np.ones(len(subs)),
               bounds=Bounds(0, 1), constraints=LinearConstraint(A, 1, np.inf),
               options={'time_limit': time_limit, 'mip_rel_gap': 0, 'presolve': True})
    out = {'id': d['id'], 'exp': d['exp'], 'variables': len(subs),
           'status': int(res.status), 'cover': None if res.x is None else round(float(res.fun)),
           'bound': getattr(res, 'mip_dual_bound', None), 'seconds': round(time.time()-t, 3)}
    if res.x is not None:
        out['selected'] = [j for j,x in enumerate(res.x) if x > .5]
    print(json.dumps(out), flush=True)
