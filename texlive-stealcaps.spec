Name:		texlive-stealcaps
Version:	64967
Release:	1
Summary:	"Steal" small capitals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stealcaps
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stealcaps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stealcaps.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stealcaps.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This little package is mainly meant to be used when there is a
(TrueType or OpenType) font that does not provide real small
capitals. As a workaround, this package helps to borrow, or
"steal", the small capitals from another font. This might also
be useful in the rare case that someone does not like the
present small capitals, and wants to change them, or likes
those from another font better. To achieve the borrowing, one
only needs to load the package and specify the name of the
target font via the from option. Package dependencies: pgfopts,
iftex, fontspec.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/stealcaps
%{_texmfdistdir}/tex/latex/stealcaps
%doc %{_texmfdistdir}/doc/latex/stealcaps

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
