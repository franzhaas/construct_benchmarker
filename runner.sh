uv sync
git clone https://github.com/franzhaas/construct.git
uv add construct
cd construct
uv run py.test tests --benchmark-only --benchmark-save=master
uv run py.test-benchmark  compare --csv=master.csv
git rebase remotes/origin/compileNumpy
git rebase remotes/origin/compilePickle
git rebase remotes/origin/compileVarInt
git rebase remotes/origin/compileTransformed
git rebase remotes/origin/compileTerminated
git rebase remotes/origin/compileStringEncoded3
git rebase remotes/origin/compileRestreamed
git rebase remotes/origin/compileChecksum
git rebase remotes/origin/CompileNullStripped
git rebase remotes/origin/compilePointerMoreInlining
uv run py.test tests --benchmark-only --benchmark-save=merged
uv run py.test-benchmark  compare --csv=merged.csv
uv run python ../analyser.py


