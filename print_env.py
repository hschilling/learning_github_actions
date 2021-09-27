import os

print('secret:', os.environ.get('MAG_KEY'))
print('secret len:', len(os.environ.get('MAG_KEY')))

