%define upstream_name    Class-Contract
%define upstream_version 1.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Class-Contract module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Contract
%{perl_vendorlib}/Class/Contract.pm
%{perl_vendorlib}/Class/demo.pl
%{_mandir}/*/*
