import io
from PIL import Image
from starlette.testclient import TestClient
from server import app

client = TestClient(app)

def test_endpoints():
    print("Testing GET / ...")
    r = client.get("/")
    assert r.status_code == 200, f"Root returned {r.status_code}"
    print("GET / passed (HTML served).")

    print("Testing GET /api/diseases ...")
    r = client.get("/api/diseases")
    assert r.status_code == 200
    data = r.json()
    assert data["count"] == 10
    print("GET /api/diseases passed (10 diseases returned).")

    print("Testing GET /api/samples ...")
    r = client.get("/api/samples")
    assert r.status_code == 200
    samples = r.json()["samples"]
    assert len(samples) == 10
    print(f"GET /api/samples passed ({len(samples)} samples returned).")

    print("Testing GET /api/model-info ...")
    r = client.get("/api/model-info")
    assert r.status_code == 200
    info = r.json()
    assert info["metrics"]["accuracy"] == 89.10
    print("GET /api/model-info passed.")

    print("Testing POST /api/predict with synthetic test leaf image...")
    # Create a 128x128 green test leaf
    img = Image.new("RGB", (128, 128), color=(34, 139, 34))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)

    files = {"file": ("test_leaf.jpg", buf, "image/jpeg")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 200, f"Predict failed: {r.text}"
    pred = r.json()["prediction"]
    print(f"POST /api/predict passed! Predicted: {pred['name']}, Confidence: {pred['confidence']}%")

    print("All backend tests PASSED successfully!")

if __name__ == "__main__":
    test_endpoints()
