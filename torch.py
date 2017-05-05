#!/usr/bin/env python

import click

from lantern import (
    analysis, modules, fitness
)


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['CIPHERTEXT'] = str(click.prompt('', prompt_suffix='', type=str))


@cli.command()
@click.pass_context
def auto(ctx):
    click.echo('auto currently unsupported')


@cli.command()
@click.pass_context
def caesar(ctx):
    decryptions = modules.caesar.crack(
        ctx.obj['CIPHERTEXT'], fitness.english.quadgrams
    )
    click.echo(decryptions[0])


@cli.command()
@click.pass_context
def substitution(ctx):
    decryptions = modules.simplesubstitution.crack(
        ctx.obj['CIPHERTEXT'], fitness.english.quadgrams
    )
    click.echo(decryptions[0])


@cli.command()
@click.pass_context
def vigenere(ctx):
    decryptions = modules.vigenere.crack(
        ctx.obj['CIPHERTEXT'],
        fitness.ChiSquared(analysis.frequency.english.quadgrams),
        max_key_period=30
    )
    click.echo(decryptions[0])


if __name__ == '__main__':
    cli(obj={})
