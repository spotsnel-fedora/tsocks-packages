%define     real_version    1.8beta5
Name:       tsocks
Version:    1.8
Release:    0.21.beta5%{?dist}
Summary:    Library for catching network connections, redirecting them on a SOCKS server
Group:      System Environment/Libraries
License:    GPLv2+
URL:        http://tsocks.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{real_version}.tar.gz
Patch0:     tsocks_remove_static_lib.patch
Patch1:     tsocks_fix_lib_path.patch
Patch2:     tsocks_script_validation_error.patch
Patch3:     tsocks_documentation_update.patch
Patch4:     tsocks-1.8-soname.patch
Patch5:     tsocks_fix_man_typo.patch
Patch6:     tsocks_include_missing_tools.patch
Patch7:     tsocks_fix_variable_types.patch
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: gcc autoconf make coreutils glibc-headers glibc-devel findutils

%description
tsocks is designed for use in machines which are firewalled from the
Internet. It avoids the need to recompile applications like lynx or
telnet so they can use SOCKS to reach the Internet. It behaves much
like the SOCKSified TCP/IP stacks seen on other platforms.

tsocks is a library to allow transparent SOCKS proxying. It wraps the
normal connect() function. When a connection is attempted, it consults
the configuration file (which is defined at configure time but defaults
to /etc/tsocks.conf) and determines if the IP address specified is local.
If it is not, the library redirects the connection to a SOCKS server
specified in the configuration file. It then negotiates that connection
with the SOCKS server and passes the connection back to the calling
program.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING FAQ TODO tsocks.conf.simple.example tsocks.conf.complex.example
%{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/libtsocks*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Tue Feb 11 2020 David Waring <david.waring2@bbc.co.uk> - 1.8-0.21.beta5
- Fixed incorrect variable types and compiler warnings about unused variables.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.20.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.19.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.18.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.17.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.16.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.15.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.14.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.13.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.12.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.11.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.10.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.9.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Jean-Francois Saucier <jsaucier@gmail.com> - 1.8-0.8.beta5
- Fix a typo in the man page
- Include the missing tools inspectsocks and validateconf

* Thu Feb 17 2011 Rex Dieter <rdieter@fedoraproject.org> 1.8-0.7.beta5
- avoid odd rpm dep mismatches by explictly specifying a soname for libtsocks

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.6.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  6 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.5.beta5
- Fix the library path problem more cleanly
- Fix bash script validation to handle the no argument case
- Change patch name to reflect guidelines
- Fix documentation to reflect patch modifications
- Remove INSTALL from packaged files

* Mon Dec 14 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.4.beta5
- Fix the library path problem on x86_64 and ppc64
- Elaborate the summary and description fields

* Sat Dec  5 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.3.beta5
- Fix as per the recommendations on bug #543566

* Thu Dec  3 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.2.beta5
- Fix Source0 URL as per the guidelines

* Tue Dec  1 2009 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 1.8-0.1.beta5
- Initial build for Fedora
