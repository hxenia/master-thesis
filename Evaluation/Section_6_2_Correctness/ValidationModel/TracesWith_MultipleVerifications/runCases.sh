python3 generateEvaluationfile.py

~/.local/bin/tamarin-prover output_cases_generated.spthy --quit-on-warning --prove | GREP_COLOR='1;32' grep -E --color=always 'verified|$' | GREP_COLOR='1;31' grep -E --color=always 'falsified|$'

