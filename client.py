import hashlib
import bisect

class ConsistentHashRing:
    """
    Consistent Hash Ring with Virtual Nodes (vnodes).
    Evenly distributes partition keys across physical nodes.
    """
    def __init__(self, vnodes_per_node=3):
        self.vnodes_per_node = vnodes_per_node
        self.ring = []
        self.nodes = set()

    def _hash(self, key_str):
        return int(hashlib.md5(key_str.encode('utf-8')).hexdigest()[:8], 16)

    def add_node(self, node_id):
        self.nodes.add(node_id)
        for v in range(self.vnodes_per_node):
            v_key = f"{node_id}#vnode{v}"
            h = self._hash(v_key)
            bisect.insort(self.ring, (h, node_id))

    def get_node(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, (h, ""))
        if idx == len(self.ring):
            idx = 0
        return self.ring[idx][1]
