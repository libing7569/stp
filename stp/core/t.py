import os
import importlib
import sys
sys.path.append('/home/vagrant/STS-dev/sts')
for i in os.listdir('../tasks/processor'):
    if '__init__.py' in i:
        continue
    module = 'tasks.processor.%s.processor' % i
    print(module)
    m = importlib.import_module(module)
    print(m.Processor.description)
    #print(m.description)

#sys.path.append('/home/vagrant/STS-dev/sts')
#m = importlib.import_module('..tasks.processor.hello_processor.processor')
#m.Processor
#print m.Processor.description
