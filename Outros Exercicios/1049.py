# entrada

ehVertebrado = input()

if (ehVertebrado == 'vertebrado'):
    ehAve = input()
    if(ehAve == 'ave'):
        ehCarnivoro = input()
        if (ehCarnivoro == 'carnivoro'):
            print('aguia')
        else:
            print('pomba')
    else:
        ehOnivoro = input()
        if (ehOnivoro == 'onivoro'):
            print('homem')
        else:
            print('vaca')
else:
    ehInseto = input()
    if(ehInseto == 'inseto'):
        ehHematofago = input()
        if(ehHematofago == 'hematofago'):
            print('pulga')
        else:
            print('lagarta')
    else:
        ehHematofago = input()
        if(ehHematofago == 'hematofago'):
            print('sanguessuga')
        else:
            print('minhoca')
