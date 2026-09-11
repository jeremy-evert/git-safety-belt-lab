# Verify the Starter State

Before changing the lab, prove the starter state works.

From the repository root, run:

```bash
python -B trail_mix.py
python -B -m unittest discover -s tests -v
```

Expected program output:

```text
Trail mix pieces: 30
Complete servings of 5: 6
```

Expected test summary:

```text
Ran 3 tests

OK
```

The exact timing may differ. The important evidence is that all three tests pass.

## Why `-B`?

Python normally creates bytecode cache files such as `__pycache__/` while it runs. The `-B` option prevents those files from being written during this beginner lab so the first `git status` stays focused on changes the student intentionally makes.

Later in Git Week we will deliberately discuss generated files, ignore rules, and repository hygiene.

## What this proves

A passing starter verification supports the claim:

> The current starter code passed these three tests in this environment.

It does **not** prove that the program is completely correct for every possible input.
