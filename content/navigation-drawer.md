Title: Android Navigation Drawer
Date: 2014-12-18 12:06
Modified: 2014-12-18 12:06
Category: Android
Tags: android
Slug: android-navigation-drawer
Authors: Vengatesh.S
<!-- Summary: "Navigation Drawer" -->

The Navigation drawer is a panel that display's the navigation option on the left side of the screen.
Navigation drawer uses the DrawerLayout API which is available in the Android Support Library. So before
proceeding make sure that have installed Android Supported Library in Android SDK.

####Create Drawer Layout:
* Declare the DrawerLayout as the root object in the android xml.
* And create a FrameLayout for the main content view of DrawerLayout.
* Then create a ListView to display content in the navigation window.

  <android.support.v4.widget.DrawerLayout
	  android:id="@+id/drawer_layout"
    	  android:layout_width="match_parent"
	  android:layout_height="match_parent"
    	  xmlns:android="http://schemas.android.com/apk/res/android">
    	  <FrameLayout
		android:id="@+id/content_frame"
		android:layout_width="match_parent"
        	android:layout_height="match_parent"/>
    	<ListView
		android:id="@+id/left_drawer"
		android:layout_width="240dp"
        	android:layout_height="match_parent"
        	android:layout_gravity="start"
        	android:background="#111"
        	android:choiceMode="singleChoice"
        	android:divider="@android:color/transparent"
        	android:dividerHeight="0dp"/>
  </android.support.v4.widget.DrawerLayout>

####Initializing the Drawer List
* Declare String array-item, ListView and DrawerLayout in the MainActivity

  String item[] = {"Create", "Read", "Help"};
  ListView listView;
  DrawerLayout drawerLayout;

* Create list_item_row.xml to list items in views.

  <TextView
	  xmlns:android="http://schemas.android.com/apk/res/android"
	  android:id="@android:id/text1"
    	  android:layout_width="match_parent"
    	  android:layout_height="wrap_content"
    	  android:textAppearance="?android:attr/textAppearanceListItemSmall"
    	  android:gravity="center_vertical"
    	  android:paddingLeft="16dp"
    	  android:paddingRight="16dp"
    	  android:textColor="#fff"
    	  android:background="?android:attr/activatedBackgroundIndicator"
    	  android:minHeight="?android:attr/listPreferredItemHeightSmall"
    />


* Declare ArrayAdapter to populate listView with its item.
* Initialize DrawerLayout and ListView with its resource ID.
* Set Adapter for list view.
* Create handler list view as OnItemClickListener.

   drawerLayout = (DrawerLayout)findViewById(R.id.drawer_layout);
   listView = (ListView)findViewById(R.id.left_drawer);
   listView.setAdapter(adapter);

   listView.setOnItemClickListener(new DrawerItemClickListener());


* Create a DrawerItemClickListener class with fragment activity to
  perform action event for navigation drawer.

  private class DrawerItemClickListener implements AdapterView.OnItemClickListener {
        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            selectItem(position);
        }

        private void selectItem(int position) {
            Fragment fragment = null;
            switch(position) {
                case 0:
                    fragment = new CreateFragment();
                    break;

                default:
                    break;
            }

            if (fragment != null) {
                FragmentManager fragmentManager = getFragmentManager();
                fragmentManager.beginTransaction().replace(R.id.content_frame, fragment).commit();

                listView.setItemChecked(position, true);
                listView.setSelection(position);
                getActionBar().setTitle(item[position]);
                drawerLayout.closeDrawer(listView);

            } else {
                Log.e("MainActivity", "Error in creating fragment");
            }
        }
    }


* Create a Fragment class and view resources.

  public class CreateFragment extends Fragment {

    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.activity_create_fragment, container, false);

        return rootView;
    }
  }


  <?xml version="1.0" encoding="utf-8"?>
  <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="com.zilogic.navigation.CreateFragment">

    <TextView android:id="@+id/txtLabel"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerInParent="true"
        android:text="Create View"
        android:textSize="16dp"/>
  </RelativeLayout>


