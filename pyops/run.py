#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 12:04:12

import os
import sys
import logging
import logging.config

import click
import pyops



@click.group(invoke_without_command=True)
@click.option('--logging-config', default=os.path.join(os.path.dirname(__file__), 'logging.conf'), help='logging conifig file for built-in python logging module', show_default=True)
@click.option('--os', default=False, is_flag=True, help='display os information ', show_default=True)
@click.option('--fs', default=False, is_flag=True, help='display fs information', show_default=True)
@click.option('--disk', default=False, is_flag=True, help='display disk information', show_default=True)
@click.version_option(version=pyops.__version__, prog_name=pyops.__name__)
@click.pass_context
def cli(ctx, **kwargs):
    pass
    #print kwargs

@cli.command()
@click.option('--dist', default='centos', help='OS distribution, default: centos')
@click.option('--version', default='7.2', help='OS version, default: 7.2')
@click.pass_context
def os(ctx, os_dist, os_version):
    pass


@cli.command()
@click.option('--type', default=False, is_flag=True, help='display fs type', show_default=True)
def fs(ctx):
    pass

def main():
    cli()


if __name__ == '__main__':
    main()
