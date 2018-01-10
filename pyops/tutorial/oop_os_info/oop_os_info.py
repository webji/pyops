#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 20:02:10

import click

from libs.os_info import OS_CI

@click.group(invoke_without_command=True)
# @click.option('--os', default=False, is_flag=True, help='display os information ', show_default=True)
@click.option('--fs', default=False, is_flag=True, help='display fs information', show_default=True)
@click.option('--disk', default=False, is_flag=True, help='display disk information', show_default=True)
@click.version_option(version='0.0.1.0', prog_name='oop_os_info')
@click.pass_context
def cli(ctx, **kwargs):
    
    if kwargs['fs']:
        print 'fs'

    if kwargs['disk']:
        print 'disk'

    return ctx



@cli.command()
@click.option('--kernel', default=False, is_flag=True, help='display kernel info', show_default=True)
@click.option('--dist_name', default=False, is_flag=True, help='display dist name', show_default=True)
@click.option('--dist_release', default=False, is_flag=True, help='display release number', show_default=True)
@click.option('--dist_codename', default=False, is_flag=True, help='display codename', show_default=True)
@click.option('--version', default=False, is_flag=True, help='display dist version', show_default=True)
@click.pass_context
def dist(ctx, kernel, dist_name, dist_release, dist_codename, version):
    g = ctx.obj
    os_info = OS_CI()
    if kernel:
        print 'Kernel: {}'.format(os_info.kernel)

    if dist_name:
        print 'Dist Name: {}'.format(os_info.dist_name)

    if dist_release:
        print 'Dist Releast: {}'.format(os_info.dist_release)

    if dist_codename:
        print 'Dist Codename: {}'.format(os_info.dist_codename)

    if version:
        print 'Dist Versoin: {}'.format(os_info.version)


if __name__ == '__main__':
    cli()
