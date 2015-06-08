#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CSS
Summary:	CSS - Object oriented access to Cascading Style Sheets (CSS)
Summary(pl.UTF-8):	CSS - zorientowany obiektowo dostęp do arkuszy CSS (Cascading Style Sheets)
Name:		perl-CSS
Version:	1.09
Release:	1
# same as Perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CSS/%{pdir}-%{version}.tar.gz
# Source0-md5:	4b86ec12e673e545a5801f40ac1c5e48
URL:		http://search.cpan.org/dist/CSS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.553
%if %{with tests}
BuildRequires:	perl-Parse-RecDescent >= 1
%endif
Requires:	perl-dirs >= 1.0-20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS module can be used, along with a CSS::Parse::* modules, to parse
CSS data and represent it as a tree of objects.

Using a CSS::Adaptor::* modules, the CSS data tree can then be
transformed into other formats.

%description -l pl.UTF-8
Modułu CSS wraz z modułami CSS::Parse::* można używać do analizy
danych CSS oraz reprezentowania ich jako drzewa obiektów.

Przy użyciu modułów CSS::Adaptor::* drzewo danych CSS można
przekształcić do innych formatów.

%prep
%setup -q -n %{pdir}-%{version}
%undos -f pm,pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a t $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CSS.pm
%{perl_vendorlib}/CSS/*.pm
%{perl_vendorlib}/CSS/Adaptor
%{perl_vendorlib}/CSS/Parse
%{_mandir}/man3/CSS.3pm*
%{_mandir}/man3/CSS::*.3pm*
%{_examplesdir}/%{name}-%{version}
