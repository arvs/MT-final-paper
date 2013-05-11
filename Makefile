LATEX = pdflatex -interaction=nonstopmode -file-line-error errordetection.tex && mv errordetection.pdf 
build:
	$(LATEX)

clean:
	rm "errordetection".*

.PHONY: build clean