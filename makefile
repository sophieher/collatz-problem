all:
	make Collatz.zip

clean:
	rm -f Collatz.html
	rm -f Collatz.log
	rm -f Collatz.zip
	rm -f RunCollatz.out
	rm -f RunCollatz.tmp
	rm -f TestCollatz.out
	rm -f *.pyc

diff: RunCollatz.in RunCollatz.out RunCollatz.py
	./RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.out RunCollatz.tmp
	rm RunCollatz.tmp

turnin-list:
	turnin --list thunt cs373pj1

turnin-submit: Collatz.zip
	turnin --submit thunt cs373pj1 Collatz.zip

turnin-verify:
	turnin --verify thunt cs373pj1

doc: Collatz.py
	pydoc -w Collatz

log:
	git log > Collatz.log

zip: makefile                                   \
             Collatz.html Collatz.log Collatz.py        \
             RunCollatz.in RunCollatz.out RunCollatz.py \
             SphereCollatz.py                           \
             TestCollatz.py TestCollatz.out
	zip -r Collatz.zip                                \
           makefile                                   \
           Collatz.html Collatz.log Collatz.py        \
           RunCollatz.in RunCollatz.out RunCollatz.py \
           SphereCollatz.py                           \
           TestCollatz.py TestCollatz.out

run: RunCollatz.in RunCollatz.py
	./RunCollatz.py < RunCollatz.in > RunCollatz.out

test: TestCollatz.py
	./TestCollatz.py > TestCollatz.out 2>&1
