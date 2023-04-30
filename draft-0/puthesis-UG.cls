%% 
%% This is file `puthesis.cls',
%% generated with the docstrip utility.
%% 
%% The original source files were:
%% 
%% puthesis.dtx  (with options: `class')
%% 
%% IMPORTANT NOTICE:
%% 
%% For the copyright see the source file.
%% 
%% You are *not* allowed to modify this file.
%% 
%% You are *not* allowed to distribute this file.
%% For distribution of the original source see
%% the terms for copying and modification in the file  puthesis.dtx.
%% 
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{puthesis-UG}
         [2011/02/16 v1.4.2 Princeton University Thesis class]
\RequirePackage{setspace}


% the next two lines are needed to make packages using xcolor happy
\RequirePackage{xcolor}
\def\current@color{ Black}
\newcounter{subyear}
\setcounter{subyear}{\number\year}
\def\submitted#1{\gdef\@submitted{#1}}
\def\@submittedyear{\ifnum\month>10 \stepcounter{subyear}\thesubyear
  \else\thesubyear\fi}
\def\@submittedmonth{\ifnum\month>10 January\else\ifnum\month>8 November
  \else\ifnum\month>6 September\else June\fi\fi\fi}
\def\adviser#1{\gdef\@adviser{#1}}
\long\def\@abstract{\@latex@error{No \noexpand\abstract given}\@ehc}
\newcommand*{\frontmatter}{
  \pagenumbering{roman}
  }
\newcommand*{\mainmatter}{\pagenumbering{arabic}}
\newcommand*{\makelot}{}
\newcommand*{\makelof}{}
\newcommand*{\makelos}{}
\newcommand*{\begincmd}{
\doublespacing
\frontmatter\maketitlepage\makeabstract
\makeacknowledgements\makedeclaration\tableofcontents\clearpage
\makelot\clearpage\makelof\clearpage\makelos
\clearpage\mainmatter}
\def\@submitted{\@submittedmonth~\@submittedyear}

\def\@dept{Mathematics}
\def\@deptpref{Department of}
\def\departmentprefix#1{\gdef\@deptpref{#1}}
\def\department#1{\gdef\@dept{#1}}
\long\def\acknowledgements#1{\gdef\@acknowledgements{#1}}
\def\dedication#1{\gdef\@dedication{#1}}
\newcommand{\maketitlepage}{{
  \thispagestyle{empty}
  \sc
  \vspace*{0in}
  \begin{center}
    \LARGE \@title
  \end{center}
  \vspace{.6in}
  \begin{center}
    \@author
  \end{center}
  \vspace{.6in}
  \begin{center}
    \sc a senior thesis submitted in partial fulfillment\\
    of the requirements for the degree of\\
     Bachelor of Arts in Mathematics at\\ Princeton University\\
  \end{center}
  \vspace{.3in}
  \begin{center}
    Adviser: \@adviser
  \end{center}
  \vspace{.3in}
  \begin{center}
    \@date
  \end{center}
  \clearpage
  }}
\newcommand*{\makeabstract}{
  \newpage
  \addcontentsline{toc}{section}{Abstract}
  \begin{center}
  \Large \textbf{Abstract}
  \end{center}
  \@abstract
  \clearpage
  }
\def\makeacknowledgements{
  \ifx\@acknowledgements\undefined
  \else
    \addcontentsline{toc}{section}{Acknowledgements}
    \begin{center}
      \Large \textbf{Acknowledgements}
    \end{center}
    \@acknowledgements
    \clearpage
  \fi
  }
\def\makedeclaration{
       \begin{center}
          {\Large \textbf{Declaration}}
       \end{center}
       
      I declare that I have not violated the Honor Code during the composition of this work. This paper represents my own work in accordance with University regulations. \\
      
      I authorize Princeton University to reproduce this thesis by photocopying or by other means, in total or in part, at the request of other institutions or individuals for the purposes of scholarly research.
  
  }
\DeclareOption{myorder}{
  \renewcommand*{\begincmd}{\doublespacing}}
\DeclareOption{lot}{\renewcommand*{\makelot}{
  \addcontentsline{toc}{section}{List of Tables}\listoftables}}
\DeclareOption{lof}{\renewcommand*{\makelof}{
  \addcontentsline{toc}{section}{List of Figures}\listoffigures}}
\DeclareOption{los}{
  \renewcommand*{\makelos}{
    \RequirePackage{losymbol}
    \section*{List of Symbols\@mkboth {LIST OF SYMBOLS}{LIST OF SYMBOLS}}
    \@starttoc{los}
    \addcontentsline{toc}{section}{List of Symbols}
  }
}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions
\LoadClass{report}
\RequirePackage[colorlinks]{hyperref}
\setlength{\oddsidemargin}{.5in}   %{.4375in}
\setlength{\evensidemargin}{.5in} %{.4375in}
\setlength{\topmargin}{-.5in}  %{-.5625in}
\setlength{\textheight}{9in}
\setlength{\textwidth}{6in}
\long\def\abstract#1{\gdef\@abstract{#1}}
\AtBeginDocument{\begincmd}
\endinput
%% 
%% End of file `puthesis.cls'.