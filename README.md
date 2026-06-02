# README-vs-Code Verifier

A bootstrap benchmark for verifying whether source code actually matches documentation claims.

## Goal

Build the smallest reproducible framework for README-vs-code verification.

Input:

* Claim
* Code

Output:

* MATCH
* LIE
* UNCERTAIN (future)

Example:

| Claim         | Code                     | Label |
| ------------- | ------------------------ | ----- |
| deletes files | os.remove(path)          | MATCH |
| deletes files | open(path,'w').write('') | LIE   |

## Why?

Documentation drift is a common problem.

Code changes constantly, but documentation is often left behind. This project explores whether a lightweight model can learn to identify when code matches—or fails to match—the claims made about it.

## Dataset Format

```csv
claim,code,label
"deletes files","os.remove(path)","MATCH"
"deletes files","open(path,'w').write('')","LIE"
```

## Version 1 Scope

Version 1 is intentionally small.

The goal is not to solve code understanding.

The goal is to validate:

1. Dataset structure
2. Labeling workflow
3. Training pipeline
4. Community contribution process

## Contributing

Contributors are encouraged to add examples from any language:

* Python
* JavaScript
* Go
* Rust
* Java
* C#
* Others

A good contribution contains both MATCH and LIE examples.

## Future Directions

* README verification
* Function-level verification
* Evidence generation
* CI/CD integration
* Benchmark creation
* Larger model experimentation

## License

MIT

