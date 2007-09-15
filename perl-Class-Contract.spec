%define real_name Class-Contract

Summary:	Class-Contract module for perl 
Name:		perl-%{real_name}
Version:	1.14
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Class::Contract module implements strong encapsulation, static
inheritance, and design-by-contract condition checking for
object-oriented Perl. The module provides a declarative syntax for
attribute, method, constructor, and destructor definitions at both
the object and class level. Pre-conditions, post-conditions, and
class invariants are also fully supported.


%prep
%setup -q -n %{real_name}-%{version} 
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


