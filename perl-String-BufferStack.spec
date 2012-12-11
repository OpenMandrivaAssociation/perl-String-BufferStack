%define upstream_name    String-BufferStack
%define upstream_version 1.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Nested buffers for templating systems
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
'String::BufferStack' provides a framework for storing nested buffers. By
default, all of the buffers flow directly to the output method, but
individual levels of the stack can apply filters, or store their output in
a scalar reference.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/String/

%changelog
* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 1.150.0-1mdv2010.1
+ Revision: 541107
- import perl-String-BufferStack


* Fri Apr 30 2010 cpan2dist 1.15-1mdv
- initial mdv release, generated with cpan2dist
