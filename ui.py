import sys
import minify
import os
from subprocess import check_output

# accept a filename
args = sys.argv
filename = args[1]

# check original length
originalcode = open(filename).read()

# run it
original_output = check_output([sys.executable, filename])

# minify it
mini = minify.minify(filename)

print mini
print 'Original length: {0}'.format(len(originalcode))
print 'Minified length: {0}'.format(len(mini))
print 'Reduction: {:.0f}%'.format(100 * (1 - len(mini) / float(len(originalcode))))

# save it
namesplit = os.path.splitext(filename)
newfilename = namesplit[0] + '_mini' + namesplit[1]
with open(newfilename, 'w') as f:
    f.write(mini)

# run the new code
new_output = check_output([sys.executable, newfilename])

if new_output != original_output:
    print "You've changed things!"
    print 'Output before:'
    print original_output
    print
    print 'Output after:'
    print new_output
    print
