# gridinfo meta packages

This repository contains different meta packages for the BDII.
BDII documentation is available at
[gridinfo documentation site](https://gridinfo-documentation.readthedocs.io/).

## Installing from packages

### On RHEL-based systems

On RHEL-based systems, it's possible to install packages from
 [EGI UMD packages](https://go.egi.eu/umd). The packages are build from this repository,
and tested to work with other components part of the Unified Middleware Distribution.

## Building packages

Individual Makefiles allowing to build source tarball and packages are provided.

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```shell
# Checkout tag to be packaged
$ git clone https://github.com/EGI-Foundation/gridinfo-meta-packages.git
$ cd gridinfo-meta-packages
$ git checkout X.X.X
# Building in a container
$ docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
[root@8a9d60c61f42 /]# yum install -y rpm-build yum-utils
# Move to the required package-specific directory
[root@8a9d60c61f42 /]# cd /source/emi-bdii-site
[root@8a9d60c61f42 emi-bdii-site]# yum-builddep -y emi-bdii-site.spec
[root@8a9d60c61f42 emi-bdii-site]# make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in
    - [CHANGELOG](CHANGELOG)
    - [gridinfo-meta-packages.spec](gridinfo-meta-packages.spec)
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
