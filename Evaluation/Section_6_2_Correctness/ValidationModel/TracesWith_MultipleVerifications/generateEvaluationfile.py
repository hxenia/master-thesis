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

#Rules
commentEnd = '// End\n'
lineRules = inputRulesFile.readline()
name = ''
while lineRules != commentEnd:
    outputFile.write(lineRules)
    #Rulename
    if lineRules.startswith('rule') & lineRules.endswith('_1:\n'): 
        name = lineRules[5:-4]
        print(name)
    if lineRules.startswith('  [ ]'):
        #write lemma
        comment = inputRulesFile.readline()
        outputFile.write('\n')
        if comment.endswith('trace exists\n'):
            outputFile.write('lemma ' + name + ':\n')
            outputFile.write(' exists-trace\n')
            outputFile.write('  "Ex #i. ' + name + '()@i"\n\n')
        if comment.endswith('no trace\n'):
            outputFile.write('lemma ' + name + ':\n')
            outputFile.write('  "not (Ex #i. ' + name + '()@i)"\n\n')
    lineRules = inputRulesFile.readline()
    

#Restrictions
inputRestrictionsPath = 'input_restrictions'
inputRestrictionsFile = open(inputRestrictionsPath, 'r')
restrictions = inputRestrictionsFile.read()

outputFile.write(restrictions)
outputFile.write('\n')

#Not equal restriction for the case rules
#outputFile.write('//Restriction for the cases\n restriction NotEqual: \n  "All a b #i. NotEqual(a, b)@i ==> not (a = b)"\n')

    
outputFile.write('\n end')

inputRulesFile.close()
outputFile.close()
inputHeadFile.close()
inputRestrictionsFile.close()
