Name:          glite-BDII_site
Version:       3.2.6
Release:       1%{?dist}
Summary:       The meta-package for the site-level BDII service.
Group:         Unknown
License:       ASL 2.0
URL:           https://github.com/EGI-Foundation/gridinfo-meta-packages
Source:        %{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires:      bdii >= 5.1.4
Requires:      bdii-config-site >= 0.6.0
Requires:      glite-info-provider-ldap >= 1.3.1
Requires:      glite-info-provider-release >= 1.0.1
Requires:      glite-info-provider-service >= 1.3.3
Requires:      glite-info-site >= 0.3.0
Requires:      glite-info-static >= 0.2.0
Requires:      glite-yaim-bdii >= 4.1.1
Requires:      glite-yaim-core >= 4.0.12
Requires:      glue-schema >= 2.0.3
Obsoletes:     glite-BDII
Obsoletes:     glite-info-generic

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
%defattr(-,root,root,-)
/opt/glite/release/%{name}-%{version}/glite-version
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Fri May 21 2010 Laurence Field <laurence.field@cern.ch> - %{version}-%{release}
- New meta-package for the site-level BDII
