Name:          emi-resource-information-service
Version:       1.1.0
Release:       1%{?dist}
Summary:       Meta-package for the resource information service
Group:         Unknown
License:       ASL 2.0
URL:           https://github.com/EGI-Foundation/gridinfo-meta-packages
Source:        %{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires:      bdii
Requires:      glue-schema
Requires:      glite-info-provider-service
Requires:      glue-validator

%description
%{summary}

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Fri Mar 17 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.1.0-1
- Build and release using GitHub Actions (#2) (Baptiste Grenier)

* Fri Sep 04 2015 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.4-1
- Removing obsolete dependencies and dependencies in yaim (Not available in CENTOS7)

* Wed Nov 14 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.3-1
- Metapackage for emi-resource-information-service including dependency on glue-validator-cron
