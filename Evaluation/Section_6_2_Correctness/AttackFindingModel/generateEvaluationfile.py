outputPath = 'output_cases_generated.spthy'
outputFile = open(outputPath, 'w')

inputHeadPath = 'input_head'
inputHeadFile = open(inputHeadPath, 'r')
head = inputHeadFile.read()
outputFile.write(head)
outputFile.write('\n')

#rules
inputRulesPath = 'input_rules'
inputRulesFile = open(inputRulesPath, 'r')

#Valid Rules
commentInvalid = '// Invalid\n'
lineRules = inputRulesFile.readline()
allValidRules = ''
validNames = []
while lineRules != commentInvalid:
    outputFile.write(lineRules)
    #Add false to rulename
    if lineRules.startswith('rule'):
        validNames.append(lineRules[5:-2])
        lineRules = lineRules[:-2] + '_false:\n'
    #replace true with false
    if lineRules.startswith('--[ Correct('):
        lineRules = '--[ In' + lineRules[4:]
    #add false to Action fact
    if lineRules.endswith('() ]->\n'):
        lineRules = lineRules[:-7] + '_false() ]->\n'
    if lineRules.endswith('()]->\n'):
        lineRules = lineRules[:-6] + '_false() ]->\n'
    allValidRules = allValidRules + lineRules
    lineRules = inputRulesFile.readline()

outputFile.write('// Dublicate Valid\n')
outputFile.write(allValidRules)

#Invalid Rules (And Wrong Format)
commentNonHonest = '// End\n'
allInvalidRules = ''
invalidNames = []
while lineRules != commentNonHonest:
    outputFile.write(lineRules)
    #Add false to rulename
    if lineRules.startswith('rule'):
        invalidNames.append(lineRules[5:-2])
        lineRules = lineRules[:-2] + '_false:\n'
    #replace true with false
    if lineRules.startswith('--[ Correct('):
        lineRules = '--[ In' + lineRules[4:]
    #add false to Action fact
    if lineRules.endswith('() ]->\n'):
        lineRules = lineRules[:-7] + '_false() ]->\n'
    if lineRules.endswith('()]->\n'):
        lineRules = lineRules[:-6] + '_false() ]->\n'
    allInvalidRules = allInvalidRules + lineRules
    lineRules = inputRulesFile.readline()

outputFile.write('// Dublicate Invalid\n')
outputFile.write(allInvalidRules)


#Restrictions
inputRestrictionsPath = 'input_restrictions'
inputRestrictionsFile = open(inputRestrictionsPath, 'r')
restrictions = inputRestrictionsFile.read()

outputFile.write(restrictions)
outputFile.write('\n')

#Not equal restriction for the case rules
outputFile.write('//Restriction for the cases\n restriction NotEqual: \n  "All a b #i. NotEqual(a, b)@i ==> not (a = b)"\n')

#Lemmas
outputFile.write('//Lemmas\n')

#valid lemmas true
outputFile.write('//Valid Aggregations with result = true\n')
i = 0
for i in range(len(validNames)):
    outputFile.write('lemma ' + validNames[i] + ':\n')
    outputFile.write(' exists-trace\n')
    outputFile.write('  "Ex #i. ' + validNames[i] + '()@i"\n\n')

#valid lemmas false
outputFile.write('//Valid Aggregations with result = false\n')
i = 0
for i in range(len(validNames)):
    outputFile.write('lemma ' + validNames[i] + '_false:\n')
    outputFile.write('  "not (Ex #i. ' + validNames[i] + '_false()@i)"\n\n')
    
#invalid lemmas true
outputFile.write('//Invalid Aggregations with result = true\n')
i = 0
for i in range(len(invalidNames)):
    outputFile.write('lemma ' + invalidNames[i] + ':\n')
    outputFile.write('  "not (Ex #i. ' + invalidNames[i] + '()@i)"\n\n')
    
#invalid lemmas false
outputFile.write('//Invalid Aggregations with result = false\n')
i = 0
for i in range(len(invalidNames)):
    outputFile.write('lemma ' + invalidNames[i] + '_false:\n')
    outputFile.write(' exists-trace\n')
    outputFile.write('  "Ex #i. ' + invalidNames[i] + '_false()@i"\n\n')
    
outputFile.write('\n end')

inputRulesFile.close()
outputFile.close()
inputHeadFile.close()
inputRestrictionsFile.close()
