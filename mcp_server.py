import sys
import json
from client import ConsistentHashRing

ring = ConsistentHashRing(5)

def handle_call(name, arguments):
    if name == "add_node":
        ring.add_node(arguments["node_id"])
        return {"nodes": list(ring.nodes), "total_vnodes": len(ring.ring)}
    elif name == "get_node":
        return {"node": ring.get_node(arguments["key"])}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
