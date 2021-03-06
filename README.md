# Hill Cipher 🔢
This project is a [Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher) type cryptography that some time ago was taught in a Math class that I attended. Please note that I am following a rule where the alphabet 'a' is at the 0th index position, not the 1st.
>In classical cryptography, the Hill cipher is a polygraphic substitution cipher based on linear algebra. Invented by Lester S. Hill in 1929, it was the first polygraphic cipher in which it was practical to operate on more than three symbols at once. The following discussion assumes an elementary knowledge of matrices. - Wikipedia
***
## Usage 💻
```python
# Import Cipher class from cipher file
from cipher import Cipher

# Set private key
c = Cipher([[1, 2], [3, 4]])
print(c.encoding2Cipher('HELLO')) # PL HZ QU
```
## API 📖
| Function name        | Description           |
| :------------- |:-------------| 
| privateKey2Matrix(private_key) | Is a function that is used to change the private_key in the form of a string into a square matrix arrangement according to the position in the alphabet. |
| matrix(position, target)      | This function will multiply each matrix by the desired plain_text. (_no need to think about the parameters, the main function has taken care of it ;)_) |
| encoding2Cipher(string) | Main function which will convert the string you entered into cipher_text. |

## To do list ✌
- [x] private_key string to matrix (privateKey2Matrix)
- [ ] Decoding
- [ ] Make it more concise

P.S: _I hope you can contribute, either tidying up my code, README, or whatever😎_