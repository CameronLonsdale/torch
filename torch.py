"""Command-line Cryptanalysis"""

import sys

import click

from lantern import analysis, modules, fitness

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-n', default=1, help="The upper limit on the number of possible decryptions to be printed")
@click.option('-v', '--verbose', is_flag=True, help="Additionally print out the key and score for each decryption")
@click.pass_context
def cli(ctx, n, verbose):
    """Command-line Cryptanalysis."""
    ctx.obj = {
        'LIMIT': n,
        'VERBOSE': verbose
    }


def read_input(ctx):
    """Read input from stdin"""
    ciphertext = str(sys.stdin.read()).rstrip()
    ctx.obj['SPACE_OUTPUT'] = ciphertext.count('\n') > 1
    return ciphertext, ctx


def output(decryptions, ctx):
    """Output decryptions using ctx"""
    verbose = ctx.obj['VERBOSE']

    for decrypt in decryptions[:ctx.obj['LIMIT']]:
        click.echo(format_output(decrypt, verbose))
        if (ctx.obj['SPACE_OUTPUT'] or verbose):
            click.echo()


def format_output(decryption, verbose):
    """Return the formatted output based on verbosity"""
    if verbose:
        return "{0}\nkey: {1}\nscore: {2}".format(decryption.plaintext, decryption.key, decryption.score)
    return decryption.plaintext


@cli.command()
@click.option('-k', '--key', default=None, type=int, help="Use this key to decrypt")
@click.pass_context
def caesar(ctx, key):
    """Decrypt or crack a caesar cipher"""
    ciphertext, ctx = read_input(ctx)
    if key:
        return click.echo(modules.caesar.decrypt(key, ciphertext))

    decryptions = modules.caesar.crack(
        ciphertext,
        fitness.english.quadgrams
    )
    output(decryptions, ctx)


@cli.command()
@click.option('-k', '--key', default=None, type=str, help="Use this key to decrypt")
@click.option('--ntrials', default=15, type=int, help="Number of trials to run the substitution cipher cracker with")
@click.pass_context
def substitution(ctx, key, ntrials):
    """Decrypt or crack a simple substitution cipher"""
    ciphertext, ctx = read_input(ctx)
    if key:
        return click.echo(modules.simplesubstitution.decrypt(key, ciphertext))

    decryptions = modules.simplesubstitution.crack(
        ciphertext,
        fitness.english.quadgrams,
        ntrials=ntrials
    )
    output(decryptions, ctx)


@cli.command()
@click.option('-k', '--key', default=None, type=str, help="Use this key to decrypt")
@click.option('-p', '--period', default=None, type=int, help="Use this key to decrypt")
@click.pass_context
def vigenere(ctx, key, period):
    """Decrypt or crack a vigenere cipher"""
    ciphertext, ctx = read_input(ctx)
    if key:
        return click.echo(modules.vigenere.decrypt(key, ciphertext))

    decryptions = modules.vigenere.crack(
        ciphertext,
        fitness.ChiSquared(analysis.frequency.english.unigrams),
        key_period=period
    )
    output(decryptions, ctx)
