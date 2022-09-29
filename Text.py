# revenu - dépense = marge

print('bienvenue à évaluateur de budget!')



le_revenu = float(input('entrer votre dépense mensuel (CFA): '))
addition = float(input('entrer vos revenu du mois prochain (CFA): '))

total_revenu = le_revenu + addition
print('créer votre revenu total le mois prochain sera de '+ str(total_revenu))
print('nous allons maintenant obtenir tout sur les dépenses...')

def rassembler_lesdépenses():
    logement = float(input('entrez vos dépenses mensuelles de logement (CFA): '))
    transport = float(input('entrez vos dépenses mensuelles de transport total (CFA): '))
    nourriture = float(input('entrez vos dépenses mensuelles de nourriture (CFA): '))
    divers = float(input('entrez vos dépenses mensuelles divers (CFA): '))
    total_dépenses = logement + transport + nourriture + divers
    return total_dépenses

dépense_total = rassembler_lesdépenses()
print('créer votre dépennse total le mois prochain sera de Cfa'+ str(dépense_total))
marge = total_revenu - dépense_total
if marge >=0:
    print('votre surplus total le mois prochain sera Cfa'+ str(marge))
else:
    print('tu monteras que Cfa' + str(marge) + 'négative!')
          
print('merci beaucoup') 