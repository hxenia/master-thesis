# master-thesis

Tamarin Prover theories, created for Masters Thesis "Aggregate Signatures in the Symbolic Model" in Computer Science

The theories are described in Detail in the thesis.

The Main theories, presented in Chapters 3, 4, and 5 are in the folder AttackScenarios. The enumeration corresponds to the enumeration presented in Section 6.1.2. For model 5 and 6, we provide oracles for the splitting zero models.

The folder AlternativeModels contains the simple equation based approach presented in Section 4.1 and the alternative representations of the index presented in Section 5.2. The second models are based on an old version of the main theories and should only demonstrate the usage of the alternative index.

Our scripts for evaluation are in the folder Evaluation. 

The correctness evaluation, presented in Section 6.2 is provided for the attack finding and for the validation models. For the validation models we have two evaluations: one for single verifications and one for multiple verifications in the same trace.
To run the Correctness evaluation scripts, run:
./runCases.sh
All lemmas should verify and be shown in green. If flasified, they are shown in red.

The Experipents presented in Section 6.3 are also provided for the attack fiding and validaiton models.
To run the experiments:
- open timeAll.py
- Choose a timeout
- set time to the choosen timeout in seconds
- create a folder "output/tamarinOutput_timeout"+time
- run: python3 timeAll.py
- If you get errors, you may have to change the path to your Tamarin instalation: in timeAll.py the variable tamarin
- The table with the measurements is in a CSV in the folder output
- The outputs of each lemma proof and timing are in a folder "output/tamarinOutput_timeout"+time
