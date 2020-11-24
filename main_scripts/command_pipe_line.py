

def command_pipe_line(commands):
    under_score = '_'
    to_be_executed = []
    for command in commands:
        words = command.split()
        function = under_score.join(words[0:2])
        del words[0:2]
        comm_and = []
        comm_with = []
        comm_vars = []
        gate = ''
        for word in words:
            if word == "and":
                gate = "and"
            elif word == "with":
                gate = "with"
            elif gate == "and":
                comm_and.append(word)
            elif gate == "with":
                comm_with.append(word)
            else:
                comm_vars.append(word)
        cmv = comm_vars
        cma = under_score.join(comm_and)
        cmw = under_score.join(comm_with)
        to_be_executed.append({function: {"vars": cmv, "and": cma, "with": cmw}})
    return to_be_executed
