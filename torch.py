import sys

import click

from lantern import (
    analysis, modules, fitness
)


@click.group()
@click.option('-n', default=1)
@click.option('-v', '--verbose', is_flag=True)
@click.pass_context
def cli(ctx, n, verbose):
    ciphertext = str(sys.stdin.read()).rstrip()
    ctx.obj = {
        'CIPHERTEXT': ciphertext,
        'LIMIT': n,
        'SPACE_OUTPUT': ciphertext.count('\n') > 1,
        'VERBOSE': verbose
    }


def output(decryptions, ctx):
    verbose = ctx.obj['VERBOSE']

    for decrypt in decryptions[:ctx.obj['LIMIT']]:
        click.echo(format_output(decrypt, verbose))
        if (ctx.obj['SPACE_OUTPUT'] or verbose):
            click.echo()


def format_output(decryption, verbose):
    if verbose:
        return "{0}\nkey: {1}\nscore: {2}".format(
            decryption.plaintext, decryption.key, decryption.score
        )
    return decryption.plaintext


@cli.command()
@click.option('-k', '--key', default=None)
@click.pass_context
def caesar(ctx, key):
    ciphertext = ctx.obj['CIPHERTEXT']
    if key:
        click.echo(modules.caesar.decrypt(key, ciphertext))
    else:
        decryptions = modules.caesar.crack(
            ciphertext, fitness.english.quadgrams
        )
        output(decryptions, ctx)


@cli.command()
@click.option('-k', '--key', default=None)
@click.option('--ntrials', default=15)
@click.pass_context
def substitution(ctx, key, ntrials):
    ciphertext = ctx.obj['CIPHERTEXT']
    if key:
        click.echo(modules.simplesubstitution.decrypt(key, ciphertext))
    else:
        decryptions = modules.simplesubstitution.crack(
            ciphertext, fitness.english.quadgrams, ntrials
        )
        output(decryptions, ctx)


@cli.command()
@click.pass_context
def vigenere(ctx):
    decryptions = modules.vigenere.crack(
        ctx.obj['CIPHERTEXT'],
        fitness.ChiSquared(analysis.frequency.english.quadgrams),
        max_key_period=30
    )
    output(decryptions, ctx)
