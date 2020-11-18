import click
import sys
import locale
import random
import difflib

def get_answer(integer=True):
    """Ask user for a answer.

    Check if answer is correct and return it
    """
    answer = input('Svar: ')
    print(type(answer))
    # answer = input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
    if not integer:
        return answer
    while not answer.isnumeric():
        # Check if user wants to quit
        if answer.lower() == 'q':
            sys.exit()
        click.echo("Svaret måste vara en siffra, försök igen")
        answer = input('Svar: ')
    return answer

def get_level():
    """Ask user what level to use"""
    level = input("Vilken nivå vill du träna på idag?: ")

    try:
        level = int(level)
    except ValueError:
        return False

    return level

def runner(level, operator='mult'):
    """docstring for runner"""
    pass


@click.group()
@click.pass_context
def cli(context):
    """Learn school stuff game"""
    context.obj = {}
    name = input('Hej! vad heter du? ')

    context.obj['name'] = name

    click.secho("Välkommen {}!!".format(name), fg='green', bg='blue')
    click.echo("Vi gör lite skolgrejer")



@cli.command()
@click.pass_context
def multi(context):
    """Spela multiplikationsspelet"""
    level = None
    while not level:
        click.echo("Ange med nivå vilken tabell du vill träna på")
        level = get_level()

    context.obj['level'] = level
    level = context.obj['level']
    name = context.obj['name']
    correct_answers = 0

    while correct_answers < 10:
        number_one = random.randint(1,max(10,level))

        click.echo("Vad är {0} * {1}?".format(level, number_one))

        true_answer = level*number_one
        answer = get_answer()
        click.clear()

        correct = False
        if int(answer) == true_answer:
            click.secho("Det stämmer att {0} * {1} = {2}, bra!\n".format(
                level, number_one, answer
            ), bg='blue', fg='green')
            correct_answers += 1
        else:
            click.secho("Tyvärr ditt svar var fel...", bg='blue', fg='red')
            click.echo("Försök igen!\n")
            correct_answers = max(0, correct_answers - 1)
        click.echo("Antal korrekta svar: {}\n".format(correct_answers))


    click.secho("GRATTIS {0} du har klarat nivå {1}!!!".format(name, level), bg='blue', fg='green')


@cli.command()
@click.pass_context
def plus(context):
    """Spela additionsspelet"""
    level = None
    while not level:
        click.echo("Ange med nivå vilken tabell du vill träna på")
        level = get_level()
    context.obj['level'] = level

    level = context.obj['level']
    name = context.obj['name']
    correct_answers = 0

    while correct_answers < 10:
        number_one = random.randint(1,max(10,level))

        click.echo("Vad är {0} + {1}?".format(level, number_one))

        true_answer = level+number_one
        answer = get_answer()
        click.clear()

        correct = False
        if int(answer) == true_answer:
            click.secho("Det stämmer att {0} + {1} = {2}, bra!\n".format(
                level, number_one, answer
            ), bg='blue', fg='green')
            correct_answers += 1
        else:
            click.secho("Tyvärr ditt svar var fel...", bg='blue', fg='red')
            click.echo("Försök igen!\n")
            correct_answers = max(0, correct_answers - 1)
        click.echo("Antal korrekta svar: {}\n".format(correct_answers))


    click.secho("GRATTIS {0} du har klarat nivå {1}!!!".format(name, level), bg='blue', fg='green')

def compare_words(words):
    """docstring for compare_words"""

    cases=[('afrykanerskojęzyczny', 'afrykanerskojęzycznym'),
           ('afrykanerskojęzyczni', 'nieafrykanerskojęzyczni'),
           ('afrykanerskojęzycznym', 'afrykanerskojęzyczny'),
           ('nieafrykanerskojęzyczni', 'afrykanerskojęzyczni'),
           ('nieafrynerskojęzyczni', 'afrykanerskojzyczni'),
           ('abcdefg','xac')]

    for a,b in words:
        print('{} => {}'.format(a,b))
        for i,s in enumerate(difflib.ndiff(a, b)):
            if s[0]==' ': continue
            elif s[0]=='-':
                print(u'Delete "{}" from position {}'.format(s[-1],i))
            elif s[0]=='+':
                print(u'Add "{}" to position {}'.format(s[-1],i))
        print()

@cli.command()
@click.argument('infile', type=click.File('r'))
@click.pass_context
def english(context, infile):
    """Engelskaläxa"""
    correct_answers = 0
    for line in infile:
        if len(line) < 5:
            continue
        line = line.split(':')
        english_word = line[0].strip().lower()
        swedish_word = line[1].strip().lower()

        # click.echo(english_word)
        # click.echo(swedish_word)
        click.echo("Vad är {0} på engelska?".format(swedish_word))

        answer = get_answer(integer=False)
        click.echo(answer)
        click.clear()

        correct = False
        if answer.lower() == english_word:
            click.secho("Det stämmer att {0} är {1} på engelska, bra!\n".format(
                swedish_word, answer
            ), bg='blue', fg='green')
            correct_answers += 1
        else:
            compare_words([(answer, english_word)])
            click.secho("Tyvärr ditt svar var fel...", bg='blue', fg='red')
            click.secho("{0} är {1} på engelska".format(swedish_word, english_word))
            click.echo("Försök igen!\n")
            correct_answers = max(0, correct_answers - 1)

    click.echo("Antal korrekta svar: {}\n".format(correct_answers))

    # click.secho("GRATTIS {0} du har klarat nivå {1}!!!".format(name, level), bg='blue', fg='green')

@cli.command()
@click.argument('infile', type=click.File('r'), required=True)
@click.pass_context
def french(context, infile):
    """French language lesson"""
    correct_answers = 0
    questions = {}
    for line in infile:
        if len(line) < 5:
            continue
        line = line.split(':')
        question = line[0].strip().lower()
        facit = line[1].strip().lower()

        # click.echo(english_word)
        # click.echo(swedish_word)
        click.echo("Vad är {0} på franska?".format(question))

        answer = get_answer(integer=False)
        click.echo(answer)
        click.clear()

        correct = False
        if answer.lower() == facit:
            click.secho("Det stämmer att {0} är {1} på franska, bra!\n".format(
                question, facit
            ))
            correct_answers += 1
        else:
            compare_words([(answer, facit)])
            click.secho("Tyvärr ditt svar var fel...", bg='blue', fg='red')
            click.secho("{0} är {1} på engelska".format(question, facit))
            click.echo("Försök igen!\n")
            correct_answers = max(0, correct_answers - 1)

    click.echo("Antal korrekta svar: {}\n".format(correct_answers))

    # click.secho("GRATTIS {0} du har klarat nivå {1}!!!".format(name, level), bg='blue', fg='green')

