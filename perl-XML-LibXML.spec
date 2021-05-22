#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-LibXML
Version  : 2.0207
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-LibXML-2.0207.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-LibXML-2.0207.tar.gz
Source1  : http://cdn-fastly.deb.debian.org/debian/pool/main/libx/libxml-libxml-perl/libxml-libxml-perl_2.0134+dfsg-1.debian.tar.xz
Summary  : 'Interface to Gnome libxml2 xml parsing and DOM library'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 MIT
Requires: perl-XML-LibXML-license = %{version}-%{release}
Requires: perl-XML-LibXML-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : libxml2-dev
BuildRequires : perl(Alien::Base)
BuildRequires : perl(Alien::Libxml2)
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(XML::NamespaceSupport)
BuildRequires : perl(XML::SAX)
BuildRequires : perl(XML::SAX::Base)
BuildRequires : perl(XML::SAX::DocumentLocator)
BuildRequires : perl(XML::SAX::Exception)
BuildRequires : perl(XML::SAX::ParserFactory)
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
INTRODUCTION
============
This module implements a Perl interface to the Gnome libxml2 library which
provides interfaces for parsing and manipulating XML files. This module allows
Perl programmers to make use of its highly capable validating XML parser and
its high performance DOM implementation.

%package dev
Summary: dev components for the perl-XML-LibXML package.
Group: Development
Provides: perl-XML-LibXML-devel = %{version}-%{release}
Requires: perl-XML-LibXML = %{version}-%{release}

%description dev
dev components for the perl-XML-LibXML package.


%package license
Summary: license components for the perl-XML-LibXML package.
Group: Default

%description license
license components for the perl-XML-LibXML package.


%package perl
Summary: perl components for the perl-XML-LibXML package.
Group: Default
Requires: perl-XML-LibXML = %{version}-%{release}

%description perl
perl components for the perl-XML-LibXML package.


%prep
%setup -q -n XML-LibXML-2.0207
cd %{_builddir}
tar xf %{_sourcedir}/libxml-libxml-perl_2.0134+dfsg-1.debian.tar.xz
cd %{_builddir}/XML-LibXML-2.0207
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-LibXML-2.0207/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-LibXML
cp %{_builddir}/XML-LibXML-2.0207/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-LibXML/b4cd683c5038b733456bfbb680f75fb1e711599a
cp %{_builddir}/XML-LibXML-2.0207/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-LibXML/e5387b6e32d15d2a5a50b4600f520f1e2665bb8b
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-LibXML/b8d8e3d6cebbef14f46031c868317e6820c9cc34
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::LibXML.3
/usr/share/man/man3/XML::LibXML::Attr.3
/usr/share/man/man3/XML::LibXML::AttributeHash.3
/usr/share/man/man3/XML::LibXML::Boolean.3
/usr/share/man/man3/XML::LibXML::CDATASection.3
/usr/share/man/man3/XML::LibXML::Comment.3
/usr/share/man/man3/XML::LibXML::Common.3
/usr/share/man/man3/XML::LibXML::DOM.3
/usr/share/man/man3/XML::LibXML::Devel.3
/usr/share/man/man3/XML::LibXML::Document.3
/usr/share/man/man3/XML::LibXML::DocumentFragment.3
/usr/share/man/man3/XML::LibXML::Dtd.3
/usr/share/man/man3/XML::LibXML::Element.3
/usr/share/man/man3/XML::LibXML::ErrNo.3
/usr/share/man/man3/XML::LibXML::Error.3
/usr/share/man/man3/XML::LibXML::InputCallback.3
/usr/share/man/man3/XML::LibXML::Literal.3
/usr/share/man/man3/XML::LibXML::Namespace.3
/usr/share/man/man3/XML::LibXML::Node.3
/usr/share/man/man3/XML::LibXML::NodeList.3
/usr/share/man/man3/XML::LibXML::Number.3
/usr/share/man/man3/XML::LibXML::PI.3
/usr/share/man/man3/XML::LibXML::Parser.3
/usr/share/man/man3/XML::LibXML::Pattern.3
/usr/share/man/man3/XML::LibXML::Reader.3
/usr/share/man/man3/XML::LibXML::RegExp.3
/usr/share/man/man3/XML::LibXML::RelaxNG.3
/usr/share/man/man3/XML::LibXML::SAX.3
/usr/share/man/man3/XML::LibXML::SAX::Builder.3
/usr/share/man/man3/XML::LibXML::SAX::Generator.3
/usr/share/man/man3/XML::LibXML::Schema.3
/usr/share/man/man3/XML::LibXML::Text.3
/usr/share/man/man3/XML::LibXML::XPathContext.3
/usr/share/man/man3/XML::LibXML::XPathExpression.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-LibXML/b4cd683c5038b733456bfbb680f75fb1e711599a
/usr/share/package-licenses/perl-XML-LibXML/b8d8e3d6cebbef14f46031c868317e6820c9cc34
/usr/share/package-licenses/perl-XML-LibXML/e5387b6e32d15d2a5a50b4600f520f1e2665bb8b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Attr.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/AttributeHash.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Boolean.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/CDATASection.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Comment.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Common.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Common.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/DOM.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Devel.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Document.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/DocumentFragment.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Dtd.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Element.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/ErrNo.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/ErrNo.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Error.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Error.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/InputCallback.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Literal.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Namespace.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Node.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/NodeList.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Number.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/PI.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Parser.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Pattern.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Reader.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Reader.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/RegExp.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/RelaxNG.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/SAX.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/SAX.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/SAX/Builder.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/SAX/Builder.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/SAX/Generator.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/SAX/Parser.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Schema.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/Text.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/XPathContext.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/XPathContext.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XML/LibXML/XPathExpression.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/XML/LibXML/LibXML.so
