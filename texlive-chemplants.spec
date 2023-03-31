Name:		texlive-chemplants
Version:	60606
Release:	2
Summary:	Symbology to draw chemical plants with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemplants
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemplants.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemplants.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers tools to draw simple or barely complex
schemes of chemical processes. The package defines several
standard symbols and styles to draw process units and streams.
The guiding light of the package is the UNICHIM regulation. All
of the symbols and styles are defined using tools of the TikZ
package, thus a basic knowledge of the logic of this powerful
tool is required to profitably use chemplants.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chemplants
%doc %{_texmfdistdir}/doc/latex/chemplants

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
