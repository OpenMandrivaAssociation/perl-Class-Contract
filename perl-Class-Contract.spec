%define upstream_name    Class-Contract
%define upstream_version 1.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Class-Contract module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Class::Contract module implements strong encapsulation, static
inheritance, and design-by-contract condition checking for
object-oriented Perl. The module provides a declarative syntax for
attribute, method, constructor, and destructor definitions at both
the object and class level. Pre-conditions, post-conditions, and
class invariants are also fully supported.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e "s,/usr/local/bin/perl,%{_bindir}/perl," demo.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Contract
%{perl_vendorlib}/Class/Contract.pm
%{perl_vendorlib}/Class/demo.pl
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.140.0-2mdv2011.0
+ Revision: 680786
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.140.0-1mdv2011.0
+ Revision: 403006
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.14-4mdv2009.0
+ Revision: 241175
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-2mdv2008.0
+ Revision: 86077
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.14-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.14-1mdk
- initial Mandriva package

