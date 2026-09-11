# Verify the Starter State

Before changing the lab, prove the starter state works.

## 1. Confirm your Python command

On Linux and macOS, use:

```bash
python3 --version
```

On Windows, one of these will commonly be available:

```powershell
py -3 --version
python --version
```

The important idea is not the spelling of the launcher. We need a working Python 3 interpreter before we use Python as evidence about the repository.

## 2. Run the starter program and tests

### Linux / macOS

From the repository root, run:

```bash
python3 -B trail_mix.py
python3 -B -m unittest discover -s tests -v
```

### Windows

If `py -3` is your Python launcher, run:

```powershell
py -3 -B trail_mix.py
py -3 -B -m unittest discover -s tests -v
```

If `python` is your working Python 3 command, use `python` in those two commands instead.

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

## A useful failure is still evidence

If a command such as `python` is not installed but `python3` is, that does not mean Git failed or the repository is broken.

It means the environment made an assumption visible.

Record the evidence, correct the assumption, and verify again.
