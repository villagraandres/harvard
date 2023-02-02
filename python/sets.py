s=set();

#add elements
s.add(1);
s.add(2);
s.add(3);
s.add(4);
s.add(3); #cannot be added because it is already in the set

s.remove(2);

print(s);

print(f"The set has {len(s)} elements")