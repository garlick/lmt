Name: 
Version: 
Release: 

License: GPL
Group: Applications/System
Summary: Lustre Montitoring Tool
URL: http://sourceforge.net/projects/lmt/
Packager: Jim Garlick <garlick@llnl.gov>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildRequires: ant, ant-nodeps
BuildRequires: mysql, mysql-devel
BuildRequires: cerebro >= 1.3-5
BuildRequires: ncurses-devel
BuildRequires: lua-devel
%if 0%{?ch4}
#BuildRequires: java-1.5.0-ibm-devel, java-1.5.0-ibm
#BuildRequires: glibc >= 2.5-18
%else
#BuildRequires: jre >= 1.4.2, java-devel >= 1.4.2
%endif
#%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
Lustre Monitoring Tool

%prep
%setup

%build
%configure
make

%install
rm -rf   $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/cerebro/*
%{_sbindir}/*
%dir %{_sysconfdir}/lmt
%config(noreplace) %{_sysconfdir}/lmt/lmt.conf
