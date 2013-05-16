LATEX = pdflatex -interaction=nonstopmode -file-line-error errordetection.tex
build:
	$(LATEX)

clean:
	rm "errordetection".*

.PHONY: build clean