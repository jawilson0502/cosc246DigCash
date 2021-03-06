import customer
import bank

alice_keys = {'e': 528, 'n': 4153}
bob_keys = {'d': 936, 'n': 4153}
amount = 100
alice_id = 123432

alice = customer.Customer(amount=amount, identity=alice_id, keys=alice_keys)
bob = bank.Bank(keys=bob_keys)

alice.blind()
bob.receive_blindmoneyorders(alice.blind_moneyorders)
bob.unblind_request()
alice.unblind(bob.to_unblind_moneyorders)
bob.receive_unblindedmoneyorders(alice.unblinded_moneyorders)
bob.receive_revealinfo(alice.reveal(bob.to_unblind_moneyorders))
bob.sign_moneyorder()
alice.receive_signature(bob.to_sign_moneyorder_key, bob.bank_signature)
alice.unblind_signed_moneyorder()
alice.print_moneyorder(alice.blind_moneyorders, 'blind')
alice.print_moneyorder(alice.unblinded_moneyorders, 'unblinded')
alice.print_moneyorder(alice.signed_moneyorder, 'signed')
alice.print_moneyorder(alice.unblindedsigned_moneyorder, 'unblindsigned')
