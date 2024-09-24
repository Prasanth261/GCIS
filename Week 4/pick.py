def check_guess(guess,answer):
    difference=guess-answer

    if difference==0:
        return 0
    elif difference>0:
        return 1
    elif difference<0:
        return -1

def test_check_guess_correct():

    #setup
    guess=4
    answer=5
    expected=-1

    #invoke
    actual=check_guess(guess,answer)

    #analys
    assert expected == actual
def test_create_guess_too_high():
    #setup
    guess=5
    answer=4
    expected=1

    actual=check_guess(guess,answer)

    assert expected==actual


def test_create_guess_too_low():
    #setup
    guess=4
    answer=5
    expected=-1

    actual=check_guess(guess,answer)

    assert expected==actual

    
