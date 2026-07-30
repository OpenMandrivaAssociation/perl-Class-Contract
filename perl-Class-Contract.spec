%define upstream_name    Class-Contract
%define upstream_version 1.14
Name:		perl-%{upstream_name}
Version:	1.14
Release:	1

Summary:	Class-Contract module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/G/GG/GGOEBEL/Class-Contract-1.14.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}
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


