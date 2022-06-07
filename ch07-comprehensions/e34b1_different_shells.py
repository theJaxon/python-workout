# In the /etc/passwd file you used earlier, what different shells (i.e., command
# interpreters, named in the final field on each line) are assigned to users? Use a
# set comprehension to gather them.

def passwd_shells(path):
    return { line.split(':')[-1].strip()
             for line in open(path)
    }

print(passwd_shells('/etc/passwd'))