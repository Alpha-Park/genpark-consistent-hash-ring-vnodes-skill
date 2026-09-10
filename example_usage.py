from client import ConsistentHashRing

def main():
    print("=== Testing Consistent Hash Ring with Virtual Nodes ===")
    ring = ConsistentHashRing(vnodes_per_node=5)
    for n in ["node-alpha", "node-bravo", "node-charlie"]:
        ring.add_node(n)

    print(f"Hash ring initialized with {len(ring.ring)} virtual node tokens.")
    keys = [f"object_blob_{i}" for i in range(5)]
    for k in keys:
        target = ring.get_node(k)
        print(f"  Key '{k}' routed to: {target}")
        assert target in ring.nodes
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
