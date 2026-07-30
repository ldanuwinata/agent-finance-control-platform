from src.services.mapping_store import MappingStore


def main():
    store = MappingStore()

    print("========== Initial Mappings ==========")
    print(store.list_mappings())

    print("\n========== Add Mapping ==========")
    store.add_mapping(
        column_name="Invoice Number",
        standard_name="Invoice",
        source="llm"
    )

    print(store.list_mappings())

    print("\n========== Get Mapping ==========")
    print(store.get_mapping("Invoice Number"))

    print("\n========== Standard Name ==========")
    print(store.get_standard_name("Invoice Number"))

    print("\n========== Has Mapping ==========")
    print(store.has_mapping("Invoice Number"))

    print("\n========== Remove Mapping ==========")
    store.remove_mapping("Invoice Number")

    print(store.list_mappings())


if __name__ == "__main__":
    main()