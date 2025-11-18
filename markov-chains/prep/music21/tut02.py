from music21 import *

dicant = corpus.parse('trecento/Fava_Dicant_nunc_iudei')
dicant.plot('histogram', 'pitch')

dicant.measures(1, 10).show()
