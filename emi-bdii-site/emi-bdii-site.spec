Name:          emi-bdii-site
Version:       1.1.0
Release:       1%{?dist}
Summary:       Meta-package for Site BDII
Group:         Unknown
License:       ASL 2.0
URL:           https://github.com/EGI-Foundation/gridinfo-meta-packages
Source:        %{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires:      emi-resource-information-service
Requires:      glite-info-provider-ldap
Requires:      bdii-config-site
Requires:      glite-info-site
Requires:      glite-info-static

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

* Fri Sep 04 2015 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.2-1
- Removing yaim dependency (which is not available in CENTOS7)

* Wed Nov 14 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.1-1
- Depend on emi-resource-information-service

* Mon Nov 12 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.0-1
- Metapackage for emi-bdii-site
